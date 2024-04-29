<script lang="ts">
	import type { Board } from '$lib/models/Board';
	import { FormData } from '$lib/models/Board';

	import CloseIcon from '$lib/assets/close_ring_duotone-1.svg';
	import SaveIcon from '$lib/assets/Done_round.svg';

	export let showModal = false;
	export let board: Board;
	export let getBoard: Function;

	let Dialog: HTMLDialogElement;

	let formData: FormData = new FormData(board.title, board.description);
	let errors: boolean = false;

	$: if (Dialog && showModal) Dialog.showModal();

	function CloseHandler() {
		showModal = false;
		errors = false;
		formData = new FormData(board.title, board.description);
	}

	async function SubmitHandler() {
		fetch(`http://localhost:8000/api/boards/${board.id}/`, {
			method: 'PATCH',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(formData.get())
		})
			.then(() => getBoard())
			.catch((error) => console.log(error))
			.finally(() => Dialog.close());
	}

	function DeleteHandler() {
		fetch(`http://localhost:8000/api/boards/${board.id}/`, {
			method: 'DELETE'
		})
			.then(() => window.location.href = '/boards')
			.catch((error) => console.log(error));
	}
</script>

<dialog
	bind:this={Dialog}
	on:close={CloseHandler}
	class="h-full rounded-lg w-full md:w-1/2 lg:w-5/12 xl:w-1/3"
>
	<div class="flex flex-col gap-7 h-full px-4 py-6">
		<header class="flex-none flex justify-between items-center">
			<h2 class="text-xl">Board details</h2>
			<button
				class="border aspect-square p-2 rounded-lg hover:bg-gray-50"
				on:click={() => Dialog.close()}
			>
				<img src={CloseIcon} alt="" />
			</button>
		</header>
		<form class="grow flex flex-col">
			<div class="grid gap-5">
				<div class="flex flex-col gap-3">
					<label for="title" class="text-xs text-gray-400 font-medium">Board title</label>
					<input
						type="text"
						name="title"
						id="title"
						class="border rounded-lg px-4 py-2 outline-none focus:outline-2"
						class:border-red-500={errors}
						class:focus:outline-red-500={errors}
						class:focus:outline-sky-500={!errors}
						placeholder="My new board"
						bind:value={formData.title}
						on:blur={() => (errors = !formData.title)}
						on:keyup={() => (errors = !formData.title)}
					/>
				</div>
				<div class="flex flex-col gap-3">
					<label for="description" class="text-xs text-gray-400 font-medium">Description</label>
					<textarea
						name="description"
						id="description"
						class="border rounded-lg px-4 py-2 outline-none focus:outline-2 focus:outline-sky-500 resize-none"
						rows="5"
						placeholder="Enter a short description"
						bind:value={formData.description}
					/>
				</div>
			</div>
			<div class="mt-auto ml-auto flex gap-3">
				<button
					type="button"
					class="flex gap-2 px-8 py-2 rounded-full border hover:bg-gray-50"
					on:click={DeleteHandler}>Delete</button
				>
				<button
					class="flex gap-2 bg-sky-500 px-8 py-2 rounded-full text-white hover:bg-sky-600 disabled:cursor-not-allowed disabled:opacity-75 disabled:hover:bg-sky-500"
					type="button"
					disabled={!formData.title}
					on:click={SubmitHandler}
				>
					Save
					<img src={SaveIcon} alt="" />
				</button>
			</div>
		</form>
	</div>
</dialog>
