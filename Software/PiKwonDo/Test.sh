coverage run PiKwonDoTest.py
#echo "#################################"
echo "Coverage:"
coverage report

cd ..

echo "Code Style:"
pycodestyle PiKwonDo/

echo "Documentation:"
pydocstyle PiKwonDo/

echo "PyLint:"
pylint PiKwonDo/
