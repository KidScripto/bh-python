import argparse
import csv
import requests


from bs4 import BeautifulSoup


# Argparser
parser = argparse.ArgumentParser(description="Receive arguments regarding target domain(s) and directory to place output csv file.")
parser.add_argument("-d", "--Domain", help="Target domain", type=str, required=False)
parser.add_argument("-of", "--OutputFile", help="Output director", type=str, required=True)
parser.add_argument("-if", "--InputFile", help="Pass a worldist file of different domains to try", required=False)
args = parser.parse_args()

# Function Definitions
def search_domain(domain):
    # Use Google search to find email addresses associated with the domain
    url = f"https://www.google.com/search?q=%40{args.Domain}&oq=%40{args.Domain}&aqs=chrome.0.35i39l2j0l4j46j69i60.9157j1j7&sourceid=chrome&ie=UTF-8"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")
    # Extract the email addresses from the search results
    emails = []
    for link in links:
        email = link.get("href")
        if email and "mailto:" in email:
            emails.append(email.split(":")[1])
    return emails

def export_to_csv(emails, domain):
    # Export the email addresses to a CSV file
    with open(f"{args.Domain}.csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Email"])
        for email in emails:
            csvwriter.writerow([email])

def search_list(InputFile):
    with open(args.InputFile, "r", newline="") as file:
        for line in file:
            url = f"https://www.google.com/search?q=%40{line}&oq=%40{line}&aqs=chrome.0.35i39l2j0l4j46j69i60.9157j1j7&sourceid=chrome&ie=UTF-8"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            links = soup.find_all("a")
            emails = []
            for link in links:
                email = link.get("href")
                if email and "mailto:" in email:
                    emails.append(email.split(":")[1])
                return emails
            
# __main__
if __name__ == "__main__":  ### Implement flow control to execute different functions depending on which input parameters were supplied
    import sys
    if len(sys.argv) < 2:
        print("Please specify a domain name")
        sys.exit()
    domain = sys.argv[1]
    emails = search_domain(args.Domain)
    export_to_csv(emails, args.Domain)
    print(f"{len(emails)} email addresses associated with {domain} have been exported to {domain}.csv")