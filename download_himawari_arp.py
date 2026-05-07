import os
import subprocess
from datetime import datetime

# =========================
# FTP账号信息
# =========================
FTP_USER = "201511210133_mail.bnu.edu.cn"
FTP_PASS = "SP+wari8"

# =========================
# 文件URL
# =========================
url = "ftp://ftp.ptree.jaxa.jp/pub/himawari/L3/ARP/031/202605/01/H09_20260501_0000_1HARP031_FLDK.02401_02401.nc"

# =========================
# 输出目录
# =========================
out_dir = "data"
os.makedirs(out_dir, exist_ok=True)

# =========================
# aria2 下载命令（优化版）
# =========================
cmd = [
    "aria2c",
    f"--ftp-user={FTP_USER}",
    f"--ftp-passwd={FTP_PASS}",
    "-x", "4",                 # ⚠️ FTP建议4线程
    "-s", "4",
    "-k", "4M",
    "--continue=true",
    "--file-allocation=none",
    "-d", out_dir,
    url
]

print("Start downloading...")
subprocess.run(cmd, check=True)

print("Download finished at:", datetime.now())
