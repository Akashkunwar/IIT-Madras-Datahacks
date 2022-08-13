import functions as fn
fn.get_data('RELIANCE.NS')
fn.show_data()
# fn.plot_data()
print(fn.df)
fn.df.to_csv('df.csv')