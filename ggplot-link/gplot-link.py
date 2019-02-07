from ggplot import *
plot1 = ggplot(mtcars,aes(x='wt',y='mpg')) + \
    geom_point() + \
    geom_abline(intercept=37,slope=-5,
                color="r",size=10)
ggplot.save(plot1,'plot.pdf')
ggplot.show(plot1)