<?php get_header(); ?>

	<div id="content" class="widecolumn">

	<?php if (have_posts()) : ?>

		<?php while (have_posts()) : the_post(); ?>

			<div class="post" id="post-<?php the_ID(); ?>">
				<div class="entry">
					<?php the_content('Read the rest of this entry &raquo;'); ?>
				</div>

				<p class="postmetadata"><small><?php the_time('F jS, Y') ?> <!-- by <?php the_author() ?> --></small> | Posted in <?php the_category(', ') ?> | <?php edit_post_link('Edit', '', ' | '); ?>  <?php comments_popup_link('No Comments &#187;', '1 Comment &#187;', '% Comments &#187;'); ?></p>
			</div>

		<?php endwhile; ?>

		

	<?php else : ?>

		<h2 class="center">Not Found</h2>
		<p class="center">Sorry, but you are looking for something that isn't here.</p>
		<?php include (TEMPLATEPATH . "/searchform.php"); ?>

	<?php endif; ?>
<div class="navigation">
			<div class="alignleft"><?php next_posts_link('&laquo; Previous') ?></div>
			<div class="alignright"><?php previous_posts_link('Next &raquo;') ?></div>
				
		</div>
	</div>



<?php get_footer(); ?>
