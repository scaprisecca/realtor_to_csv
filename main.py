from homeharvest import scrape_property
from datetime import datetime
import os

# Global variables
location = "46205"
listing_type = "for_sale"
past_days = 180
property_type = ['multi_family']

# Create scraped_listings directory if it doesn't exist
os.makedirs('scraped_listings', exist_ok=True)

# Generate filename based on current timestamp
current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"scraped_listings/HomeHarvest_{location}_{property_type}_{current_timestamp}.csv"

properties = scrape_property(
    location=location,
    listing_type=listing_type,  # or (for_sale, for_rent, pending)
    past_days=past_days,  # sold in last 30 days - listed in last 30 days if (for_sale, for_rent)
    property_type=property_type,
  # date_from="2023-05-01", # alternative to past_days
  # date_to="2023-05-28",
  # foreclosure=True
  # mls_only=True,  # only fetch MLS listings
)
print(f"Number of properties: {len(properties)}")

# Export to csv
properties.to_csv(filename, index=False)
print(properties.head())