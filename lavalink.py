from os import system, environ

class lavalinkserver:

    def __init__(self):
        self.download_command = "curl -s https://api.github.com/repos/Frederikam/Lavalink/releases/22355850 | grep browser_download_url | cut -d '\"' -f 4 | wget -qi -"
        self.change_port = 'sed -i "s|DYNAMICPORT|$PORT|" application.yml'
        self.change_password = 'sed -i "s|DYNAMICPASSWORD|$PASSWORD|" application.yml'
        self.no_password = 'sed -i "s|DYNAMICPASSWORD|youshallnotpass|" application.yml'
        self.additional = environ.get("ADDITIONAL_JAVA_OPTIONS")
        self.run_command = f"java -jar Lavalink.jar {self.additional}"

    def password_and_port(self):
        print("[INFO] Changing the port and password...")
        try:
            system(self.change_port)
            if not environ.get("PASSWORD"):
               print("[INFO] No password found in the enviroment, default password has been set...")
               return system(self.no_password)
            system(self.change_password)
        except BaseException as exc:
            print(f"[ERROR] Error changing port and password... Info: {exc}")
        else:
            print("[INFO] Successfully changed port and password...")

    def download(self):
        print("[INFO] Downloading lavalink...")
        try:
            system(self.download_command)
        except BaseException as exc:
            print(f"[ERROR] Error downloading lavalink... Info: {exc}")

        else:
            print("[INFO] Successfully downloaded lavalink...")
    
    def run(self):
        self.download()
        self.password_and_port()
        print("[INFO] Starting the lavalink server...")
        try:
            system(self.run_command)
        except BaseException as exc:
            print(f"[ERROR] Failed to start the lavalink server... Info: {exc}")

if __name__ == "__main__":
   lavalinkserver().run()