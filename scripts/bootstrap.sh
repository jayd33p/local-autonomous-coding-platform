# Example bootstrap script for local development

set -e

echo "Creating python venv and installing backend dependencies..."
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd -

if [ -d frontend ]; then
  echo "Installing frontend dependencies..."
  cd frontend
  npm install
  cd -
fi

echo "Bootstrap complete. Run backend: cd backend && . .venv/bin/activate && uvicorn app.main:app --reload"
