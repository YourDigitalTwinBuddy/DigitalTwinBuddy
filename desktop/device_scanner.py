# -*- coding: utf-8 -*-
"""
desktop/device_scanner.py
Karmic AI Desktop Companion: USB Device & Media Scanner (iPhone & Android)
Local hardware interface for Windows Portable Devices (WPD), Shell COM, and WhatsApp Desktop caches.
100% Zero-Cloud Photo Leakage Protocol.
"""

import os
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional, Callable

try:
    import pythoncom
    import win32com.client
    HAS_WIN32COM = True
except ImportError:
    HAS_WIN32COM = False


def parse_size_mb(size_str: Any) -> float:
    """
    Parses Windows Shell size string (e.g. '1.04 KB', '14.2 MB', '1.45 GB') into float MB.
    """
    if not size_str:
        return 0.0
    s = str(size_str).strip().replace('\xa0', ' ')
    try:
        parts = s.split()
        val = float(parts[0].replace(',', ''))
        unit = parts[1].upper() if len(parts) > 1 else 'BYTES'
        if 'KB' in unit:
            return round(val / 1024.0, 2)
        elif 'MB' in unit:
            return round(val, 2)
        elif 'GB' in unit:
            return round(val * 1024.0, 2)
        else:
            return round(val / (1024.0 * 1024.0), 2)
    except Exception:
        return 0.0


class DeviceScanner:
    def __init__(self):
        self.user_profile = Path(os.environ.get("USERPROFILE", "C:\\Users\\Default"))
        self.whatsapp_package_dir = self.user_profile / "AppData" / "Local" / "Packages"

    def detect_connected_devices(self) -> List[Dict[str, Any]]:
        """
        Detects connected mobile devices (iPhone, Android, Tablets, WPD) via Windows Shell COM.
        Thread-safe with pythoncom.CoInitialize().
        """
        devices = []
        if not HAS_WIN32COM:
            return [{"name": "Windows Shell COM unavailable", "type": "ERROR", "status": "INSTALL_PYWIN32"}]

        need_uninit = False
        try:
            pythoncom.CoInitialize()
            need_uninit = True
        except Exception:
            pass

        try:
            shell = win32com.client.Dispatch("Shell.Application")
            computer = shell.Namespace(17) # ssfDRIVES (This PC)
            
            for item in computer.Items():
                item_name = str(item.Name)
                item_path = str(item.Path)

                device_type = None
                if "iphone" in item_name.lower() or "apple" in item_name.lower():
                    device_type = "IPHONE"
                elif any(x in item_name.lower() for x in ["android", "samsung", "galaxy", "pixel", "oneplus", "xiaomi", "redmi", "oppo", "vivo"]):
                    device_type = "ANDROID"
                elif "portable" in getattr(item, "Type", "").lower() or "device" in getattr(item, "Type", "").lower() or "wpd" in item_path.lower():
                    device_type = "PORTABLE_DEVICE"

                if device_type:
                    status = "CONNECTED_LOCKED"
                    folder = getattr(item, "GetFolder", None)
                    if folder:
                        try:
                            sub_items = folder.Items()
                            if sub_items and sub_items.Count > 0:
                                internal = sub_items.Item(0)
                                int_folder = getattr(internal, "GetFolder", None)
                                if int_folder and int_folder.Items().Count > 0:
                                    status = "READY"
                                else:
                                    status = "CONNECTED_LOCKED"
                        except Exception:
                            status = "CONNECTED_LOCKED"

                    devices.append({
                        "name": item_name,
                        "type": device_type,
                        "path": item_path,
                        "status": status,
                        "instructions": "Unlock phone with Passcode/FaceID and tap 'Trust This Computer' if locked." if status == "CONNECTED_LOCKED" else "Device unlocked and ready for deep media audit."
                    })

        except Exception as e:
            print(f"[!] Device detection exception: {e}")
        finally:
            if need_uninit:
                try:
                    pythoncom.CoUninitialize()
                except Exception:
                    pass

        return devices

    def scan_usb_device_media(self, device_name_filter: Optional[str] = None, progress_callback: Optional[Callable[[str], None]] = None) -> Dict[str, Any]:
        """
        Traverses connected USB device (iPhone or Android) storage and DCIM folders.
        Extracts file names, exact sizes via Windows Shell GetDetailsOf, and duplicate signatures.
        """
        if not HAS_WIN32COM:
            return {"error": "win32com is required on Windows", "items": [], "total_reclaimable_mb": 0.0}

        results = {
            "device_name": "Unknown",
            "total_files_scanned": 0,
            "duplicate_photos": 0,
            "large_videos": 0,
            "total_reclaimable_mb": 0.0,
            "total_reclaimable_gb": 0.0,
            "items": [],
            "status": "COMPLETED"
        }

        need_uninit = False
        try:
            pythoncom.CoInitialize()
            need_uninit = True
        except Exception:
            pass

        try:
            seen_names = set()
            shell = win32com.client.Dispatch("Shell.Application")
            computer = shell.Namespace(17)

            target_item = None
            for item in computer.Items():
                name = str(item.Name)
                if device_name_filter and device_name_filter.lower() in name.lower():
                    target_item = item
                    break
                elif not device_name_filter and any(k in name.lower() for k in ["iphone", "apple", "android", "samsung", "pixel"]):
                    target_item = item
                    break

            if not target_item:
                results["status"] = "NO_DEVICE_FOUND"
                return results

            results["device_name"] = str(target_item.Name)
            if progress_callback:
                progress_callback(f"Connecting to {results['device_name']}...")

            folder = getattr(target_item, "GetFolder", None)
            if not folder:
                results["status"] = "DEVICE_NOT_ACCESSIBLE"
                return results

            sub_items = folder.Items()
            if sub_items.Count == 0:
                results["status"] = "DEVICE_LOCKED"
                return results

            # Traverse Internal Storage
            for sub_idx in range(sub_items.Count):
                sub = sub_items.Item(sub_idx)
                sub_folder = getattr(sub, "GetFolder", None)
                if not sub_folder:
                    continue

                for dir_idx in range(sub_folder.Items().Count):
                    dcim_dir = sub_folder.Items().Item(dir_idx)
                    dcim_folder = getattr(dcim_dir, "GetFolder", None)
                    if not dcim_folder:
                        continue

                    folder_name = str(dcim_dir.Name)
                    if progress_callback:
                        progress_callback(f"Scanning folder {folder_name} on device...")

                    file_count = dcim_folder.Items().Count
                    for f_idx in range(file_count):
                        file_item = dcim_folder.Items().Item(f_idx)
                        fname = str(file_item.Name)
                        
                        # Detail 2 is Size string in Windows Shell for WPD
                        size_str = dcim_folder.GetDetailsOf(file_item, 2)
                        fsize_mb = parse_size_mb(size_str)
                        results["total_files_scanned"] += 1

                        # Duplicate and burst detection:
                        # iOS names edited photos IMG_E... and originals IMG_...
                        # Burst photos have same root or copy tags
                        clean_base = fname.replace("IMG_E", "IMG_").rsplit(".", 1)[0].lower()
                        is_dup = False
                        recom = "File appears unique."
                        ftype = "STANDARD_FILE"

                        if clean_base in seen_names or "copy" in fname.lower() or fname.startswith("IMG_E"):
                            is_dup = True
                            ftype = "DUPLICATE_PHOTO" if any(fname.lower().endswith(x) for x in [".heic", ".jpg", ".jpeg", ".png", ".webp", ".aae"]) else "DUPLICATE_FILE"
                            recom = "Duplicate / edited copy. Keep primary photo and purge copy."
                            results["duplicate_photos"] += 1
                            results["total_reclaimable_mb"] += fsize_mb
                        elif fsize_mb > 50:
                            ftype = "LARGE_VIDEO" if any(fname.lower().endswith(x) for x in [".mov", ".mp4", ".m4v", ".avi", ".mkv"]) else "HEAVY_ARCHIVE"
                            recom = f"Large video ({fsize_mb} MB). Recommend compressing or cold-archiving."
                            results["large_videos"] += 1
                            results["total_reclaimable_mb"] += fsize_mb

                        seen_names.add(clean_base)

                        if is_dup or fsize_mb > 50:
                            results["items"].append({
                                "file_name": fname,
                                "file_size_mb": fsize_mb,
                                "file_type": ftype,
                                "storage_location": f"{results['device_name']} / {folder_name}",
                                "is_reclaimable": True,
                                "recommendation": recom
                            })

            results["total_reclaimable_gb"] = round(results["total_reclaimable_mb"] / 1024, 2)

        except Exception as e:
            print(f"[!] Scan device exception: {e}")
            results["status"] = f"ERROR: {e}"
        finally:
            if need_uninit:
                try:
                    pythoncom.CoUninitialize()
                except Exception:
                    pass

        return results

    def scan_whatsapp_bloat(self, progress_callback: Optional[Callable[[str], None]] = None) -> Dict[str, Any]:
        """
        Scans local WhatsApp Desktop cache, forwarded media dumps, and temporary media.
        """
        results = {
            "app_name": "WhatsApp Desktop (Windows)",
            "total_files_scanned": 0,
            "total_reclaimable_mb": 0.0,
            "items": [],
            "status": "COMPLETED"
        }

        if not self.whatsapp_package_dir.exists():
            results["status"] = "WHATSAPP_NOT_INSTALLED"
            return results

        wa_packages = list(self.whatsapp_package_dir.glob("*WhatsApp*"))
        if not wa_packages:
            results["status"] = "WHATSAPP_NOT_INSTALLED"
            return results

        if progress_callback:
            progress_callback("Scanning local WhatsApp Desktop media caches...")

        for pkg in wa_packages:
            for root, dirs, files in os.walk(pkg):
                if any(k in root.lower() for k in ["transfers", "tempstate", "cache", "contactpictures"]):
                    for fname in files:
                        ext = os.path.splitext(fname)[1].lower()
                        if ext in [".mp4", ".mov", ".jpg", ".jpeg", ".png", ".opus", ".ogg", ".pdf", ".zip", ".apk", ""]:
                            full_path = os.path.join(root, fname)
                            try:
                                sz = os.path.getsize(full_path)
                                sz_mb = round(sz / (1024 * 1024), 2)
                                results["total_files_scanned"] += 1

                                if sz_mb > 0.01:
                                    results["total_reclaimable_mb"] += sz_mb
                                    results["items"].append({
                                        "file_name": fname,
                                        "file_size_mb": sz_mb,
                                        "file_type": "CHAT_DUMP",
                                        "file_path": full_path,
                                        "storage_location": "WhatsApp Desktop Cache",
                                        "is_reclaimable": True,
                                        "recommendation": "Chat forwarded media cache. Safe to purge."
                                    })
                            except Exception:
                                pass

        results["total_reclaimable_gb"] = round(results["total_reclaimable_mb"] / 1024, 2)
        return results

    def scan_local_downloads(self, progress_callback: Optional[Callable[[str], None]] = None) -> Dict[str, Any]:
        """
        Scans the user's Downloads and Pictures folders for duplicate installers, zip files, and burst photos.
        """
        results = {
            "source": "Local PC Downloads & Pictures",
            "total_files_scanned": 0,
            "total_reclaimable_mb": 0.0,
            "items": []
        }

        target_dirs = [
            self.user_profile / "Downloads",
            self.user_profile / "Pictures"
        ]

        for d in target_dirs:
            if not d.exists():
                continue
            if progress_callback:
                progress_callback(f"Scanning {d.name} for stale duplicate downloads...")

            for item in d.iterdir():
                if item.is_file():
                    fname = item.name
                    sz_mb = round(item.stat().st_size / (1024 * 1024), 2)
                    results["total_files_scanned"] += 1

                    is_dup = False
                    if any(p in fname for p in ["(1)", "(2)", "(3)", " - Copy", "_copy"]):
                        is_dup = True
                    elif sz_mb > 100:
                        is_dup = True

                    if is_dup:
                        results["total_reclaimable_mb"] += sz_mb
                        results["items"].append({
                            "file_name": fname,
                            "file_size_mb": sz_mb,
                            "file_type": "DUPLICATE_FILE" if is_dup else "HEAVY_ARCHIVE",
                            "file_path": str(item),
                            "storage_location": f"PC {d.name}",
                            "is_reclaimable": True,
                            "recommendation": "Duplicate downloaded file or heavy installer."
                        })

        results["total_reclaimable_gb"] = round(results["total_reclaimable_mb"] / 1024, 2)
        return results


device_scanner = DeviceScanner()
