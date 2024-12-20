import yagmail
import argparse

def send_email(file_path, recipient_email):
    try:
        fp=str(f"{file_path}.zip")
        yag = yagmail.SMTP("yourmail@gmail.com", "your app pass")
        yag.send(
            to=recipient_email, 
            subject="Zipped Images", 
            contents="Find the attached zip file.", 
            attachments=fp
        )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send email with attachment")
    parser.add_argument("file_path")
    parser.add_argument("recipient_email")
    args = parser.parse_args()

    send_email(args.file_path, args.recipient_email)
