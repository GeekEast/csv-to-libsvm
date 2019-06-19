### Prerequisite
- Python3
- Git
### Data Preprocessing
- Clear or convert string in csv file
- move the lable or testing data into first column
### Start
- Input file: fars.csv
- Output file: libsvm.data
- Headers: true for header, false for no-header
```sh
git clone git@github.com:GeekEast/csv-to-libsvm.git && cd csv-to-libsvm
python3 csvtosvm.py fars.csv libsvm.data false
```
