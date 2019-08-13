# Comparison of most star projects in different languages on GITHUB

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

language_list = ['Python','C','JavaScript','Java','Ruby','Go','Perl','Haskell']
plot_dicts = []
for language in language_list:
	url = 'https://api.github.com/search/repositories?q=language:{}&sort=stars'\
	.format(language)
	r = requests.get(url)
	print('Status code:', r.status_code)
	response_dict = r.json()
	
	repo_dicts = response_dict['items']
	def fn():
		for repo_dict in repo_dicts[:1]:
			plot_dict = {
				'value': repo_dict['stargazers_count'],             
				'xlink': repo_dict['html_url'],
				}
			plot_dicts.append(plot_dict)
		return plot_dicts
	fn()

my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.show_legend = False
my_config.title_fontsize = 18
my_config.label_fontsize = 14
my_config.major_label_font_size = 20
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Comparison of most star projects in different languages on GITHUB'
chart.x_labels = language_list


chart.add('', plot_dicts)
chart.render_to_file('Comparison of most star projects in different languages on GITHUB.svg')
