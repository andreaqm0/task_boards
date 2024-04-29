<script lang="ts">
	import type { Task } from '$lib/models/Task';
	import EditTaskModal from '../modals/EditTaskModal.svelte';
	
	export let task: Task;
	export let index: number;
	let showModal = false;
</script>

<button
	class="flex items-start rounded-2xl p-4 gap-5 cursor-pointer hover:scale-105"
	class:bg-gray-200={task.status === null}
	class:bg-amber-300={task.status === 'progress'}
	class:bg-green-300={task.status === 'done'}
	class:bg-red-300={task.status === 'cancelled'}
	on:click={() => (showModal = true)}
>
	{#if task.icon}
		<div
			class="flex-none flex justify-center items-center rounded-xl bg-white aspect-square size-14"
		>
			<img src="/emojis/{task.icon}.png" class="size-6" alt="emoji" />
		</div>
	{/if}
	<div class="grow text-start py-1">
		<h2 class="text-xl font-medium leading-10">{task.name}</h2>
		<p class="w-10/12">
			{task.description}
		</p>
	</div>
	{#if task.status}
		<div
			class="flex-none my-auto rounded-xl aspect-square p-3"
			class:bg-yellow-500={task.status === 'progress'}
			class:bg-red-500={task.status === 'cancelled'}
			class:bg-green-500={task.status === 'done'}
		>
			<img src="/{task.status}.svg" class="size-7" alt="" />
		</div>
	{/if}
</button>
<EditTaskModal bind:showModal bind:task {index} />
