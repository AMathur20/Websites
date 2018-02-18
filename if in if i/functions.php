<?php
function the_excerpt() {
	echo apply_filters('the_excerpt', get_the_excerpt());
}


function get_the_excerpt($fakeit = true) {
	global $id, $post;
	$output = '';
	$output = $post->post_excerpt;
	if ( !empty($post->post_password) ) { // if there's a password
		if ( $_COOKIE['wp-postpass_'.COOKIEHASH] != $post->post_password ) {  // and it doesn't match the cookie
			$output = __('There is no excerpt because this is a protected post.');
			return $output;
		}
	}

	return apply_filters('get_the_excerpt', $output);
}

?>