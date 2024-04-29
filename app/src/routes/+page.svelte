<script>
	import Logo from '$lib/assets/Logo.svg';
</script>

<div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 grid gap-10">
	<div class="flex items-center gap-5">
		<a href="/"><img src={Logo} alt="logo" /></a>
		<h1 class="text-4xl font-medium">My Task Board</h1>
	</div>
	<a
		href="/boards"
		class="text-amber-950 rounded-full bg-amber-500 hover:bg-amber-600 py-2 px-8 w-fit mx-auto"
	>
		See All Boards
	</a>
</div>
