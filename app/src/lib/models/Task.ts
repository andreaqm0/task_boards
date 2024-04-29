export interface TaskBase {
	name: string;
	description: string;
	icon: string | null;
	status: string | null;
	board: number;
}

export interface Task extends TaskBase {
	id: number;
	created_at: string;
	updated_at: string;
}

export class FormData {
	public name: string;
	public description: string;
	public icon: string | null;
	public status: string | null;

	constructor(
		name = '',
		description = '',
        icon: string = 'work',
        status: string | null = null
	) {
		this.name = name;
		this.description = description;
		this.icon = icon;
		this.status = status;
	}

	get() {
		return {
			name: this.name,
			description: this.description,
			icon: this.icon,
			status: this.status
		};
	}
}
