import csv
import requests
from bs4 import BeautifulSoup

def search_emails(domain):
    # Use Google search to find email addresses associated with the domain
    url = f"https://www.google.com/search?q=%40{domain}&oq=%40{domain}&aqs=chrome.0.35i39l2j0l4j46j69i60.9157j1j7&sourceid=chrome&ie=UTF-8"
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
    with open(f"{domain}.csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Email"])
        for email in emails:
            csvwriter.writerow([email])

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please specify a domain name")
        sys.exit()
    domain = sys.argv[1]
    emails = search_emails(domain)
    export_to_csv(emails, domain)
    print(f"{len(emails)} email addresses associated with {domain} have been exported to {domain}.csv")