My goal is to design a pp_blog using a pelican tool. For that content took from 'https://blog.packetp.com/'. 
I used a third party theme for a pleasant look and search content plugin. Steps are followed below

1. After pelican installation, generated default blog by using 'pelican-quickstart' command. Inputs are given like blog,  author name and path directory is defined. And the rest of the options selected are default. 

2. Go to the blog main directory, and change directory to content. Here, we created two directories, One is for blog which contains blog articles and another one is pages(Contains about and contact-us pages) 

3. For blog articles, we took the content from 'https://blog.packetp.com/'. Go to each blog article written in that and ported the entire article to markdown file type. 

4. And in the pages directory, created 'about.md' and 'contact.md'. Content written about company information. 

5. Changed to main directory and created theme directory. Download the elegant theme here (Sources: https://github.com/Pelican-Elegant/elegant). The path of this theme is included in 'pelicanconf.py'.

6. Changed to main directory and created plugin directory. Download the  tipue_search plugin. (Sources : https://github.com/getpelican/pelican-plugins/tree/master/tipue_search). The path of this plugin is included in 'pelicanconf.py'. 

7. Then build and run the blog.
