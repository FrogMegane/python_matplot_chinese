# -*- coding: utf-8 -*-
from __future__ import unicode_literals
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\Fonts\msjh.ttc", size=20)
year=[103,103.5,104,104.5,105,105.5]
grade=[89.67,90.84,93.12,95.12,95.39,96.24]
x_ticks_labels = [u'103上',u'103下',u'104上',u'104下',u'105上',u'105下']
gl= [u'(1/111)',u'(1/111)',u'(1/39)',u'(1/39)',u'(1/36)',u'(1/36)']

fig, ax = plt.subplots(1,1) 
ax.scatter(year,grade)
ax.plot(year,grade)
for x,y,v in zip(year,grade,gl):
    ax.text(x-0.4,y+0.3,v, fontsize=10, fontproperties=font)

# Set number of ticks for x-axis
ax.grid()
ax.set_xticks(year)
ax.set_title('歷年成績與系排名', fontsize=18, fontproperties=font)
# Set ticks labels for x-axis
ax.set_xticklabels(x_ticks_labels, fontsize=12, fontproperties=font)
ax.set_xlabel('學期', fontsize=12, fontproperties=font)
ax.set_ylabel('平均', fontsize=12, fontproperties=font)