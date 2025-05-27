from homeharvest import scrape_property
from datetime import datetime
import os
import time

def scrape_location(location_config):
    """
    Scrape properties for a single location configuration.
    
    Args:
        location_config (dict): Dictionary containing location configuration
            Expected keys: location, listing_type, past_days, property_type
    """
    try:
        print(f"\nProcessing location: {location_config['location']}")
        
        # Generate filename based on current timestamp and location
        current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_location = location_config['location'].replace(",", "").replace(" ", "_")
        filename = f"scraped_listings/{safe_location}_{current_timestamp}.csv"
        
        print(f"Fetching properties with config: {location_config}")
        
        # Scrape properties with the current configuration
        properties = scrape_property(
            location=location_config['location'],
            listing_type=location_config['listing_type'],
            past_days=location_config['past_days'],
            property_type=location_config['property_type'],
            # date_from="2023-05-01", # alternative to past_days
            # date_to="2023-05-28",
            # foreclosure=True
            # mls_only=True,  # only fetch MLS listings
        )
        
        print(f"Found {len(properties)} properties")
        
        # Export to csv if we found properties
        if len(properties) > 0:
            properties.to_csv(filename, index=False)
            print(f"Saved results to {filename}")
            print(properties.head())
        else:
            print("No properties found for this configuration")
            
        # Be nice to the servers
        time.sleep(5)
        return True
        
    except Exception as e:
        print(f"Error processing {location_config.get('location', 'unknown location')}: {str(e)}")
        return False

def main():
    # Create scraped_listings directory if it doesn't exist
    os.makedirs('scraped_listings', exist_ok=True)
    
    # Define locations to scrape with their configurations
    locations_config = [
        {
            "location": "Indianapolis, IN",
            "listing_type": "for_sale",
            "past_days": 180,
            "property_type": ["multi_family"]
        },
        {
            "location": "Indianapolis, IN",
            "listing_type": "for_rent",
            "past_days": 180,
            "property_type": ["multi_family"]
        },
        {
            "location": "Indianapolis, IN",
            "listing_type": "sold",
            "past_days": 180,
            "property_type": ["multi_family"]
        },
        {
            "location": "Chandler, AZ",
            "listing_type": "for_sale",
            "past_days": 90,
            "property_type": ["single_family"]
        },
        {
            "location": "Gilbert, AZ",
            "listing_type": "for_sale",
            "past_days": 90,
            "property_type": ["single_family"]
        },
        # Add more locations as needed following the same format
        # {
        #     "location": "Chicago, IL",
        #     "listing_type": "for_sale",
        #     "past_days": 90,
        #     "property_type": ["single_family"]
        # },
    ]
    
    print(f"Starting to process {len(locations_config)} locations")
    
    # Process each location configuration
    success_count = 0
    for config in locations_config:
        if scrape_location(config):
            success_count += 1
    
    print(f"\nCompleted! Successfully processed {success_count} out of {len(locations_config)} locations")

if __name__ == "__main__":
    main()
