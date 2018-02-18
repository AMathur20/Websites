<div id="footer">
	
	<p>
	<strong>
		&copy; Copyright 2005-<?php echo date("Y")." "; bloginfo('name'); ?>. All rights reserved.
	</strong>
	<br /> <?php wp_loginout(); ?> <?php echo $wpdb->num_queries; ?> queries. <?php timer_stop(1); ?> seconds.
	<br /><br />
	<a href="http://www.blogtopsites.com/photo-blog/">
		<img border="0" src="http://www.blogtopsites.com/tracker.php?do=in&amp;id=28476" alt="Top Photo Blog Blogs" />
	</a>
	&nbsp;&nbsp;&nbsp;&nbsp;
	<a href="http://www.Bloghub.com/">
		<img src="http://www.Bloghub.com/images/80x15.gif" alt="Blog Directory &amp; Search engine" width="80" height="15" border="0" />
	</a>
	&nbsp;&nbsp;&nbsp;&nbsp;
	<a href="http://validator.w3.org/check?uri=referer">
		<img src='http://ifinifi.anksconsulting.com/wp-content/xhtml10.gif' alt='Valid XHTML 1.0' border="0"/>
	</a>
	&nbsp;&nbsp;&nbsp;&nbsp;
	<a href="http://jigsaw.w3.org/css-validator/check/referer">
		<img src='http://ifinifi.anksconsulting.com/wp-content/valid-css.png' alt='Valid CSS' border="0"/>
	</a>

</p>

	<?php do_action('wp_footer'); ?>
</div>
</div>

<br /><br />

</body>
</html>
