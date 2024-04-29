<script lang="ts">
	import type { Board } from "$lib/models/Board";
    export let board: Board;
</script>

<a href="/boards/{board.id}" class="flex flex-col justify-between gap-5 rounded-lg border px-4 py-6 divide-y divide-dashed sm:hover:scale-105 hover:bg-slate-50">
    <div class="flex flex-col gap-y-2">
        <h2 class="text-xl font-semibold">{board.title}</h2>
        <p class="truncate">{board.description}</p>
    </div>
    <div class="pt-5 text-sm font-mono">
        tasks: {board.tasks.length}
    </div>
</a>