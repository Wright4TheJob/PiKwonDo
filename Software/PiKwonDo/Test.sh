echo "-------------------"
echo "Build Documentation"
echo "-------------------"
cd ../../docs
make html

cd ../Software/pikwondo

echo "------------------"
echo "Test Documentation"
echo "------------------"
pydocstyle $PWD


# echo "Code Style:"
# pycodestyle pikwondo/

echo "------"
echo "PyLint"
echo "------"
pylint $PWD

echo "---------"
echo "Unit Test"
echo "---------"

coverage run unit_test.py
#echo "#################################"
# echo "Coverage:"
coverage report
