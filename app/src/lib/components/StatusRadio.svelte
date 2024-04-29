<script lang="ts">
	export let group: string | null;
	export let name: string;
	export let id: string
	export let value: string;
	export let text: string;
	export let img;
</script>

<li>
	<input type="radio" {name} {value} {id} class="sr-only peer" bind:group />
	<label
		for={id}
		class={`
            flex items-center gap-5
            w-full p-1 rounded-lg cursor-pointer
            border 
            peer-checked:border-blue-600
            hover:border-blue-600
        `}
	>
		<div
			class="aspect-square p-3 rounded-lg"
			class:bg-green-500={value === 'done'}
			class:bg-amber-500={value === 'progress'}
			class:bg-red-500={value === 'cancelled'}
		>
			<img src={img} alt="" class="size-5" />
		</div>
		{text}
	</label>
</li>
