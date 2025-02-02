# Creating 'f' string example

my_website = {'body':{'font': 'verdana', 'font-size': 20, 'background-color': 'lightgray', 'padding': 2},
              'nav':{'padding-top': 70, 'padding-bottom': 70},
              'container':{'font': 'verdana', 'font-size': 20, 'background-color': 'lightgray', 'padding': 2},
              'footer':{'background-color': 'dimgray', 'color': 'white', 'font-size': 16}}
# print(my_website)
for index, selector in enumerate(my_website.keys(), start=1):
    # print(index, selector, my_website[selector])
    print(f"{index:<2d}- Selector: {selector:9s} properties and values: {my_website[selector]}")