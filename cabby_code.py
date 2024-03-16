from cabby import create_client

# Create a Cabby client
client = create_client(
    'localhost',
    use_https=False,
    port='1234', # Adjusted port based on your server configuration
    discovery_path='/services/discovery-a'
)

# Set authentication
client.set_auth(
    username='admin', # Adjust username and password as per your server configuration
    password='admin',
    # Uncomment and specify the JWT auth URL if using JWT-based authentication
    # jwt_auth_url='/management/auth'
)

# Discover services to ensure the inbox service is available
services = client.discover_services()
print(f"Services: {services}")

# Read the STIX 2.x JSON data from your file
with open("campagne.stx.json") as stix_file:
    stix_data = stix_file.read()

# Specify the STIX 2.x JSON binding
binding = 'urn:stix.mitre.org:stix:json:2.0'

# Use the inbox service to push the data to the TAXII server
client.push(stix_data, binding,
            collection_names=['collection-a'], # Adjust the collection name as per your server configuration
            uri='/services/inbox-a') # Adjust the inbox service URI as per your server configuration

print("Successfully exported to TAXII server.")
