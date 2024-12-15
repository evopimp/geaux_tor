def connect_to_tor():
    from stem import Signal
    from stem.control import Controller
    import requests

    def create_session():
        session = requests.Session()
        session.proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        return session

    def verify_connection(session):
        try:
            response = session.get('http://httpbin.org/ip')
            return response.json()
        except Exception as e:
            print(f"Error verifying connection: {e}")
            return None

    session = create_session()
    connection_status = verify_connection(session)
    
    if connection_status:
        print("Connected to Tor network successfully.")
        return session
    else:
        print("Failed to connect to Tor network.")
        return None