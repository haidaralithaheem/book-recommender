# Install required Python dependencies
pip install -r requirements.txt

# Create Streamlit config directory and configuration file
mkdir -p ~/.streamlit/
echo " \
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
