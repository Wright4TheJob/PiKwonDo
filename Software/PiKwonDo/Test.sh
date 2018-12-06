echo "-------------------"
echo "Build Documentation"
echo "-------------------"
cd ../../docs
make html

cd ../Software

echo "------------------"
echo "Test Documentation"
echo "------------------"
pydocstyle pikwondo/


# echo "Code Style:"
# pycodestyle pikwondo/

echo "------"
echo "PyLint"
echo "------"
pylint pikwondo/

cd pikwondo
echo "---------"
echo "Unit Test"
echo "---------"

coverage run unit_test.py
#echo "#################################"
# echo "Coverage:"
coverage report
