import type { Task } from './Task';

export interface BoardBase {
	title: string;
	description: string;
}

export interface Board extends BoardBase {
	id: number;
	tasks: Task[];
	created_at: string;
	updated_at: string;
}

export class FormData {
	public title: string;
	public description: string;

	constructor(title = '', description = '') {
		this.title = title;
		this.description = description;
	}

	get() {
		return {
			title: this.title,
			description: this.description
		};
	}
}
