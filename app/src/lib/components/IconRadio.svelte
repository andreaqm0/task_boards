<script lang="ts">
	export let group: string | null;
	export let name: string;
	export let id: string
	export let value: string;
	export let img;
</script>

<li>
	<input type="radio" {name} {value} {id} class="sr-only peer" bind:group />
	<label
		for={id}
		class={`
            flex items-center justify-center
            w-full p-3 rounded-lg cursor-pointer
            bg-slate-200
            peer-checked:bg-amber-200
            hover:bg-slate-300 
        `}
	>
		<img src={img} alt="" class="size-6" />
	</label>
</li>
