python main.py

git add .
git commit -m "'"
git push

robocopy .\public ..\warriorthesis\ /E
cd ..
cd warriorthesis
git add .
git commit -m "'"
git push
cd ..
cd warriorthesis_compiler