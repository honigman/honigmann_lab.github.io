import pandas as pd
from collections import defaultdict

# Define the path for the input CSV file and the output HTML file
csv_file_path = r"C:\Users\osho799e\Downloads\scopus.csv"  # Replace with your actual CSV file path
output_html_path = r"C:\Users\osho799e\Lab_WebPage\test\bib_publications.html"  # Replace with your desired output path

# Load the CSV file
publications_data = pd.read_csv(csv_file_path)

# Group publications by year
publications_by_year = defaultdict(list)
for _, row in publications_data.iterrows():
    year = str(row["Year"]).strip()
    authors_raw = row["Authors"]
    title = str(row["Title"]).strip()
    source_title = str(row["Source title"]).strip()
    volume = str(row["Volume"]).strip() if not pd.isna(row["Volume"]) else ""
    issue = str(row["Issue"]).strip() if not pd.isna(row["Issue"]) else ""
    page_start = str(row["Page start"]).strip() if not pd.isna(row["Page start"]) else ""
    page_end = str(row["Page end"]).strip() if not pd.isna(row["Page end"]) else ""
    doi = str(row["DOI"]).strip() if not pd.isna(row["DOI"]) else ""

    # Format authors (split by semicolons and trim spaces)
    authors = ", ".join([author.strip() for author in authors_raw.split(";")])

    # Format pages
    pages = f"{page_start}-{page_end}" if page_start and page_end else ""

    # Add publication to the group
    pub_entry = {
        "authors": authors,
        "title": title,
        "source_title": source_title,
        "volume": volume,
        "issue": issue,
        "pages": pages,
        "year": year,
        "doi": doi,
    }
    publications_by_year[year].append(pub_entry)

# Sort publications by year (descending order)
sorted_years = sorted(publications_by_year.keys(), reverse=True)

# Generate HTML content
publications_html = ""
for year in sorted_years:
    publications_html += f"<h2>{year}</h2>\n<ul>\n"
    for pub in publications_by_year[year]:
        # Wrap the title in the link if DOI is available
        title_html = (
            f"<a href='https://doi.org/{pub['doi']}' target='_blank' "
            f"style='color: inherit; text-decoration: none;'><strong>{pub['title']}</strong></a>"
            if pub['doi']
            else f"<strong>{pub['title']}</strong>"
        )

        # Add publication details
        publication_entry = (
            f"<li>{title_html} ({pub['year']})<br>"
            f"{pub['authors']}<br>"
            f"<strong><em>{pub['source_title']}</em></strong>"
        )

        publication_entry += "</li>\n<br>\n"
        publications_html += publication_entry
    publications_html += "</ul>\n"
publications_html += ""


# Save the generated HTML to a file
with open(output_html_path, "w", encoding="utf-8") as file:
    file.write(publications_html)

print(f"HTML content for publications has been generated in '{output_html_path}'!")
