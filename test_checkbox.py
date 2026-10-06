from playwright.sync_api import Page,expect
import pytest

def text_radio_button(page : Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 1.select specific checkbox
    sunday_checkbox=page.get_by_label("Sunday")
    sunday_checkbox.check()
    expect(sunday_checkbox).to_be_checked()

    #2.count the number of checkbox
     #setup 1
    days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    checkboxes=[]

    #setup2
    for day in days:
      checkbox= page.get_by_label(day)
      checkboxes.append(checkbox)

# simple way
    checkboxes=[page.get_by_label(day) for day in days]
    print("total number of checkbox:",len(checkboxes))

# 3.select all the checkboxes and assert each checkbox is selected
    for checkbox in checkboxes:
         checkbox.check()
         expect(checkbox).to_be_checked()

# 4 check the last three checkboxes

    for checkbox in checkboxes[-3:]:
         checkbox.uncheck()
         expect(checkbox).not_to_be_checked()

#toggle check boxes
    for checkbox in checkboxes:
        if checkbox.is_checked():
             checkbox.uncheck()
             expect(checkbox).not_to_be_checked()
    else:
             checkbox.check()
             expect(checkbox).to_be_checked()

# randomly select the checkbox eg 1,3,5
   indexes=[1,3,5]

for i in indexes:
   checkboxes[i].check()
   expect(checkboxes[i]).to_be_checked()

# 7 select the checkbox base on label/ input value
weekday='Friday'
for label in weekday:
    if label==weekday:
        checkbox= page.get_by_label(label)
        checkbox.check()
        expect(checkbox).to_be_checked()









