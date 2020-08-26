rem chrome
pytest -v -s -m "sanity" --html=./Reports/sanity_new_report.html testCases/ --browser chrome
rem pytest -v -s -m "sanity or regression" --html=./Reports/sanityORregression_new_report.html testCases/ --browser chrome
rem pytest -v -s -m "sanity and regression" --html=./Reports/sanityANDregression_new_report.html testCases/ --browser chrome
rem pytest -v -s -m "regression" --html=./Reports/regression_new_report.html testCases/ --browser chrome

rem firefox
rem pytest -v -s -m "sanity" --html=./Reports/sanity_new_report1.html testCases/ --browser firefox
rem pytest -v -s -m "sanity or regression" --html=./Reports/sanityORregression_new_report1.html testCases/ --browser firefox
rem pytest -v -s -m "sanity and regression" --html=./Reports/sanityANDregression_new_report1.html testCases/ --browser firefox
rem pytest -v -s -m "regression" --html=./Reports/regression_new_report1.html testCases/ --browser firefox
