import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BC4ktLajQJwhxJdTR2peqojTKQnj9t--JsdKo7YxmQh2c8yyYf_XT7ps4FdfId3Mc3cP6fkqpG0WJoQ2PGzarFtGfsszhbPJF0I9-_sd0VjzpE7IBd7iLkpdrCRs8-DXJ8Y1oDLL6pAQ'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()