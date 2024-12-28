from pybtex.database import parse_file
from collections import defaultdict
import latexcodec

# Define the path for the input .bib file and the output HTML file
bib_file_path = r"C:\Users\osho799e\Downloads\preprints_bibtext.bib"  # Replace with your actual .bib file path
output_html_path = r"C:\Users\osho799e\Lab_WebPage\test\preprint_publications.html"  # Replace with your desired output path

# Load the .bib file
bib_data = parse_file(bib_file_path)

# Group publications by year
publications_by_year = defaultdict(list)
for entry in bib_data.entries.values():
    # Extract fields with fallback for missing data
    year = entry.fields.get("year", "Unknown Year").strip()
    title = entry.fields.get("title", "No Title").strip()
    source_title = entry.fields.get("journal", entry.fields.get("booktitle", "Unknown Source")).strip()
    volume = entry.fields.get("volume", "").strip()
    issue = entry.fields.get("number", "").strip()
    pages = entry.fields.get("pages", "").strip()
    doi = entry.fields.get("doi", "").strip()

    # Decode LaTeX fields and remove curly braces
    title = title.encode('utf-8').decode('latex').replace("{", "").replace("}", "")
    source_title = source_title.encode('utf-8').decode('latex').replace("{", "").replace("}", "")

    # Process authors and remove curly braces
    authors = ", ".join(
        [
            " ".join(
                name.encode('utf-8').decode('latex').replace("{", "").replace("}", "")
                for name in person.first_names + person.last_names
            )
            for person in entry.persons.get("author", [])
        ]
    )

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
