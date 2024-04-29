<script lang="ts">
	import { FormData } from '$lib/models/Task';

	import CloseIcon from '$lib/assets/close_ring_duotone-1.svg';
	import CancelIcon from '$lib/assets/cancel.svg';
	import SaveIcon from '$lib/assets/Done_round.svg';

	import WorkEmoji from '$lib/assets/emojis/work.png';
	import SpeechEmoji from '$lib/assets/emojis/speech.png';
	import CoffeeEmoji from '$lib/assets/emojis/coffee.png';
	import WeightlifterEmoji from '$lib/assets/emojis/weightlifter.png';
	import BooksEmoji from '$lib/assets/emojis/books.png';
	import ClockEmoji from '$lib/assets/emojis/clock.png';

	import ProgressIcon from '$lib/assets/Time_atack_duotone.svg';
	import DoneIcon from '$lib/assets/Done_round_duotone.svg';
	import CancelledIcon from '$lib/assets/close_ring_duotone.svg';

	import IconRadio from '../IconRadio.svelte';
	import StatusRadio from '../StatusRadio.svelte';

	export let showModal = false;
	export let boardId: number;
	export let getBoard: Function;

	let Dialog: HTMLDialogElement;

	let formData = new FormData();
	let errors = false;

	$: if (Dialog && showModal) Dialog.showModal();
	$: if (formData) console.log(formData);

	function CloseHandler() {
		showModal = false;
		errors = false;
		formData = new FormData();
	}

	function SubmitHandler() {
		fetch('http://localhost:8000/api/tasks/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ ...formData.get(), board: boardId })
		})
			.then(() => getBoard())
			.catch((err) => console.log(err))
			.finally(() => Dialog.close());
	}
</script>

<dialog
	bind:this={Dialog}
	on:close={CloseHandler}
	class="h-full rounded-lg w-full md:w-1/2 lg:w-5/12 xl:w-1/3"
>
	<div class="flex flex-col gap-7 h-full px-4 py-6">
		<header class="flex-none flex justify-between items-center">
			<h2 class="text-xl">Add new task</h2>
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
					<label for="title" class="text-xs text-gray-400 font-medium">Task name</label>
					<input
						type="text"
						name="title"
						id="title"
						placeholder="My new task"
						class="border rounded-lg px-4 py-2 outline-none focus:outline-2"
						class:border-red-500={errors}
						class:focus:outline-red-500={errors}
						class:focus:outline-sky-500={!errors}
						bind:value={formData.name}
						on:blur={() => (errors = !formData.name)}
						on:keyup={() => (errors = !formData.name)}
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
				<div class="flex flex-col gap-3">
					<label for="icon" class="text-xs text-gray-400 font-medium">Icon</label>
					<ul role="radiogroup" class="grid grid-flow-col gap-3 w-fit">
						<IconRadio
							bind:group={formData.icon}
							name="add-icon"
							id="add-work"
							value="work"
							img={WorkEmoji}
						/>
						<IconRadio
							bind:group={formData.icon}
							name="add-icon"
							id="add-speech"
							value="speech"
							img={SpeechEmoji}
						/>
						<IconRadio
							bind:group={formData.icon}
							name="add-icon"
							id="add-coffee"
							value="coffee"
							img={CoffeeEmoji}
						/>
						<IconRadio
							bind:group={formData.icon}
							name="add-icon"
							id="add-weightlifter"
							value="weightlifter"
							img={WeightlifterEmoji}
						/>
						<IconRadio
							bind:group={formData.icon}
							name="add-icon"
							id="add-books"
							value="books"
							img={BooksEmoji}
						/>
						<IconRadio
							bind:group={formData.icon}
							name="add-icon"
							id="add-clock"
							value="clock"
							img={ClockEmoji}
						/>
					</ul>
				</div>
				<div class="flex flex-col gap-3">
					<div class="flex items-center gap-3">
						<label for="status" class="text-xs text-gray-400 font-medium">Status</label>
						<button
							type="button"
							class:invisible={!formData.status}
							on:click={() => (formData.status = null)}
							class="rounded-full hover:bg-gray-100"><img src={CancelIcon} alt="" /></button
						>
					</div>
					<ul role="radiogroup" class="grid sm:grid-cols-2 gap-3">
						<StatusRadio
							bind:group={formData.status}
							name="add-status"
							id="add-progress"
							value="progress"
							text="In Progress"
							img={ProgressIcon}
						/>
						<StatusRadio
							bind:group={formData.status}
							name="add-status"
							id="add-done"
							value="done"
							text="Completed"
							img={DoneIcon}
						/>
						<StatusRadio
							bind:group={formData.status}
							name="add-status"
							id="add-cancelled"
							value="cancelled"
							text="Won't do"
							img={CancelledIcon}
						/>
					</ul>
				</div>
			</div>
			<div class="mt-auto ml-auto flex gap-3">
				<button
					type="button"
					class="flex gap-2 px-8 py-2 rounded-full border hover:bg-gray-50"
					on:click={() => Dialog.close()}>Cancel</button
				>
				<button
					class="flex gap-2 bg-sky-500 px-8 py-2 rounded-full text-white hover:bg-sky-600 disabled:cursor-not-allowed disabled:opacity-75 disabled:hover:bg-sky-500"
					type="button"
					disabled={!formData.name}
					on:click={SubmitHandler}
				>
					Save
					<img src={SaveIcon} alt="" />
				</button>
			</div>
		</form>
	</div>
</dialog>
