import os
import argparse

def run_pipeline(keyword, max_num, Down_storage_dir, Con_storage_dir, scale_percent,Scale_storage_dir,Zip_storage_dir,  recipient_email):
    os.system(f"python download.py {keyword} \"{max_num}\" \"{Down_storage_dir}\"")
    os.system(f"python convertToGreyscale.py \"{Down_storage_dir}\" \"{Con_storage_dir}\"")
    os.system(f"python scale.py \"{Con_storage_dir}\" \"{Scale_storage_dir}\" {scale_percent}")
    os.system(f"python zip.py \"{Scale_storage_dir}\" \"{Zip_storage_dir}.zip\"")
    os.system(f"python sendToEmail.py \"{Zip_storage_dir}.zip\" \"{recipient_email}\"")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword")
    parser.add_argument("max_num", type=int)
    parser.add_argument("downstorage_dir")
    parser.add_argument("const")
    parser.add_argument("scale_percent", type=int)
    parser.add_argument("scstorage_dir")
    parser.add_argument("zipstorage_dir")
    parser.add_argument("recipient_email")

    args = parser.parse_args()
    run_pipeline(args.keyword, args.max_num, args.downstorage_dir, args.const,args.scale_percent,  args.scstorage_dir, args.zipstorage_dir, args.recipient_email)
