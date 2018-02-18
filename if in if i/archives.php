<?php
/*
Template Name: Archives
*/
?>
<?php get_header(); ?>
<div id="content">
<?php query_posts( 'posts_per_page=-1' ); ?>
<div id="thumbs">
  <?php if (have_posts()) : ?>
<ul>	
    <?php while (have_posts()) : the_post();
    remove_filter('the_excerpt', 'wpautop');
     ?>	
    
      <li>
        <a href="<?php the_permalink(); ?>"><?php the_excerpt(); ?></a>
      </li>
      
    <?php endwhile; ?>
</ul>
  <?php endif; ?>
</div>
</div>
<?php get_footer(); ?>