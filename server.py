import http.server
import socketserver
import socket
import webbrowser
import os
import sys

# Ensure UTF-8 output for Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PORT = 8080

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS and caching headers for smooth mobile loading
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    local_ip = get_local_ip()
    url_local = f"http://localhost:{PORT}"
    url_phone = f"http://{local_ip}:{PORT}"

    print("=" * 60)
    print("  [+] RotaMaster - Mobil Rota Optimizasyon Sunucusu")
    print("=" * 60)
    print(f"\n[+] Bilgisayarınızdan açmak için:")
    print(f"    -> {url_local}")
    print(f"\n[+] Aynı Wi-Fi ağındaki TELEFONUNUZDAN açmak için:")
    print(f"    -> {url_phone}")
    print("\n[i] IPUCU: Bilgisayarınızda açılan sayfada sağ üstteki 'QR Kod'")
    print("    simgesine tıklayıp telefon kameranızla okutarak da açabilirsiniz!\n")
    print("=" * 60)
    print("Durdurmak için Ctrl + C tuşlarına basın.\n")

    # Automatically open local browser
    try:
        webbrowser.open(url_local)
    except Exception:
        pass

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nSunucu kapatildi.")

if __name__ == "__main__":
    main()
