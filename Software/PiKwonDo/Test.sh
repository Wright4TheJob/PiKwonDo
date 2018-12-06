coverage run unit_test.py
#echo "#################################"
echo "Coverage:"
coverage report

cd ..

echo "Code Style:"
pycodestyle pikwondo/

echo "Documentation:"
pydocstyle pikwondo/

echo "PyLint:"
pylint pikwondo/
