import pyshorteners
import re, sys, socket

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


def style(text, color):
    return f"{color}{text}{Colors.RESET}"


def print_error(message):
    print(style(message, Colors.FAIL))


def print_info(message):
    print(style(message, Colors.OKCYAN))


def print_success(message):
    print(style(message, Colors.OKGREEN))


def validate_url(url):
    newurl = url.lower()
    if "http" in newurl and "://" in url:
        return newurl
    else:
        return ""

def validate_domain(domain):
    pattern = re.compile(r'^[A-Za-z0-9.]+$')

    if pattern.match(domain):
        return True
    else:
        return False


def internet_connection():
    try:
        socket.gethostbyname("www.google.com")
        return True
    except socket.gaierror:
        return False


def home_logo():
    print(style("""
██    ██ ██████  ██          ███    ███  █████  ███████ ██  ██ 
██    ██ ██   ██ ██          ████  ████ ██   ██ ██      ██  ██  
██    ██ ██████  ██          ██ ████ ██ ███████ ███████ █████   
██    ██ ██   ██ ██          ██  ██  ██ ██   ██      ██ ██  ██  
 ██████  ██   ██ ███████     ██      ██ ██   ██ ███████ ██   ██ 
""", Colors.OKCYAN))
    print(style("Nithin 3>: Navigating the Digital Realm with Code and Security - Where Programming Insights Meet Cyber Vigilance.", Colors.OKBLUE))

def about():
    print(style("""Welcome to IHA089, your premier source for cutting-edge cybersecurity solutions. At IHA089, we specialize in developing tools designed to enhance the security and integrity of your digital environment. 

We understand the importance of reliable and efficient cybersecurity solutions, which is why we focus on creating tools that are not only powerful but also user-friendly. Our tools are designed to streamline security processes, making it easier for organizations to protect their assets and maintain a secure operational framework.
    """, Colors.OKGREEN))


def validate_phishing_keyword(keyword):
    pattern = re.compile(r'^[a-zA-Z0-9-_]+$')

    if pattern.match(keyword):
        return True
    else:
        return False

def shorting_url(short_obj, url):
    try:
        short_url =  short_obj.short(url)
        return short_url
    except:
        print("An error occur when short url")
        return "error"

def shortener_service(url):
    print(style("1\tTinyURL\n2\tDAGd\n3\tCLCKRU", Colors.OKGREEN))
    try:
        select = int(input(style("Select an option [1-3]: ", Colors.OKBLUE)))
        shortner = pyshorteners.Shortener()
        if select == 1:
            shorter = shortner.tinyurl
            return shorting_url(shorter, url)
        elif select == 2:
            shorter = shortner.dagd
            return shorting_url(shorter, url)
        elif select == 3:
            shorter = shortner.clckru
            return shorting_url(shorter, url)
        else:
            print_error("Please select a number between 1 and 3.")
            return "error"
    except ValueError:
        print_error("Please select a number between 1 and 3.")
        return "error"

def combiner(masked_url, domain_name, phishing_keyword):
    mskd = masked_url.split("://")
    url_header = mskd[0]
    url_tail = mskd[1]
    if phishing_keyword == "":
        result = url_header+"://"+domain_name+"@"+url_tail
    else:
        result = url_header+"://"+domain_name+"-"+phishing_keyword+"@"+url_tail

    return result

def urlmask():
    try:
        aa = sys.argv[1]
        if aa == "about":
            home_logo()
            about()
            return 0
    except:
        pass

    home_logo()

    try:
        original_url = input("Enter original url[Ex. https://google.com]:")
    except KeyboardInterrupt:
        print("\nExit by user")
        return 0
    if original_url == "":
        print_error("Please enter a URL.")
        return 0

    check_url_valid = validate_url(original_url)
    if check_url_valid == "":
        print_error("URL is not valid, please enter a correct URL (Ex: https://google.com).")
        return 0

    masked_url = shortener_service(original_url)
    if masked_url == "error":
        return 0

    try:
        domain_nam = input("Enter what domain you want to set[Ex. google.com, facebook.com]:")
    except KeyboardInterrupt:
        print("\nExit by user")
        return 0

    domain_name = domain_nam.lower()
    if domain_name == "":
        print_error("Please enter a domain name.")
        return 0
    if not validate_domain(domain_name):
        print_error("Please enter a correct domain name (Ex: google.com, facebook.com).")
        return 0

    try:
        phishing_key = input("Do you want to enter phising keyword[yes/no]:")
    except KeyboardInterrupt:
        print("\nExit by user")
        return 0

    if phishing_key == "yes" or phishing_key == "YES":
        try:
            phishing_keyword = input("Enter phishing keyworkd[Ex: free, login]:")
        except KeyboardInterrupt:
            print("\nExit by user")
            return 0
        phishing_keyword = phishing_keyword.lower()
        if not validate_phishing_keyword(phishing_keyword):
            print_error("Please enter a valid phishing keyword using letters, numbers, '-' or '_'.")
            return 0
    else:
        phishing_keyword = ""
    
    result = combiner(masked_url, domain_name, phishing_keyword)
    print_success("Masked URL::: {}".format(result))
    
if __name__ == "__main__":
    urlmask()