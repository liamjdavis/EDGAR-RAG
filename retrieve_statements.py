from edgar import get_filings, Company
from edgar import *
import os

# Set your identity
set_identity("Liam Davis davisliam123@gmail.com")

tickers = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "INTC", "CSCO", "ORCL", "ADBE",
    "JNJ", "PFE", "MRK", "ABBV", "AMGN", "GILD", "BMY", "LLY", "BIIB", "REGN",
    "JPM", "BAC", "WFC", "C", "GS", "MS", "AXP", "SCHW", "BLK", "V",
    "PG", "KO", "PEP", "UL", "CL", "KMB", "MDLZ", "GIS", "K", "HSY",
    "VZ", "T", "TMUS", "F", "GM", "TSLA", "BA", "CAT", "MMM", "DUK", "NEE", "SO"
]

forms = [
    '10-K', '10-Q', '8-K', 'S-1', '14-A'
]

form_count = len(forms)

# # Ensure the statements directory exists
# os.makedirs("statements", exist_ok=True)

# for i, ticker in enumerate(tickers):
#     company = Company(ticker)
    
#     form = forms[i % form_count]
    
#     filings = company.get_filings()
#     filings.filter(form=form)
#     filing = filings.latest()
    
#     markdown = filing.markdown()
    
#     # Define the file path
#     file_path = os.path.join("statements", f"{ticker}_{form}.md")
    
#     # Save the markdown content to the file
#     with open(file_path, "w") as file:
#         file.write(markdown)
    
#     print(f"Markdown file saved successfully for {ticker} - {form}.")

# Make a testing dir for testing
os.makedirs("testing", exist_ok=True)
filings = get_filings()

for i in range(5):
    filing = filings[i]
    markdown = filing.markdown()
    
    # Define the file path
    file_path = os.path.join("testing", f"{i}.md")
    
    # Save the markdown content to the file
    with open(file_path, "w") as file:
        file.write(markdown)
    
    print(f"Markdown file saved successfully for {filing}.")
