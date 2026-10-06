from playwright.sync_api import Page,expect
import pytest

def test_static_table(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # locating the table
    table= page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()

    # 2 count the total number of row in table
    row=table.locator("tr")
    expect(row).to_have_count(7)
    # print the count
    row_count=row.count()
    print("how many number of row:-",row_count)
    page.wait_for_timeout(5000)

    # 3 count the total number of columns/header in the table
    column=row.locator("th")
    expect(column).to_have_count(4)

    # print the count
    columns_count=column.count()
    print("how many columns count :",columns_count)
    page.wait_for_timeout(5000)

    # 4.Read the all data from 2nd row of the table
    second_row=row.nth(2).locator("td")
    second_row_text=second_row.all_inner_texts()
    print("2nd row data=====>",second_row_text)

    expect(second_row).to_have_text(['Learn Java', 'Mukesh', 'Java', '500'])
    page.wait_for_timeout(5000)

    print("2nd row of data.....")
    for text in second_row_text:
        print(text)

  #  read the all data from table
    all_row_data=row.all()

    print("printing the all data row ")
    for texts in all_row_data[1:]:
       cols= texts.locator("td").all_inner_texts()
       print(cols)
       page.wait_for_timeout(5000)

# print the book name whose author name is "mukesh"
    print("print the book name written by mukesh")
    for texts in all_row_data[1:]:
       author_name= texts.locator("td").inner_text()
       if author_name=='Mukesh':
           book_name=texts.locator("td").inner_text()
           print(f"{author_name} \t {book_name}")

# 6.calculate total price of all the book

    total_price=0
    for texts in all_row_data[1:]:
       price= texts.locator("td").nth(3).inner_text()
       total_price+=int(price)
       print("total_price",total_price)










