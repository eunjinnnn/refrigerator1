<script>
    let data = "DELETE";
    import { Input, Label, Button, Select, Card, Alert } from 'flowbite-svelte';

    let lists = [];
    let cat_selected = '';
    let unit_selected = '';
    let volume = '';
    let foodname = '';
    let purchaseDate = '';
    let expirationDate = '';

    let categories = [
        { value: 1, name: 'VEGETABLES' },
        { value: 2, name: 'DRINKS' },
        { value: 3, name: 'FROZEN FOOD' },
        { value: 4, name: 'ETC' }
    ];

    let units = [
        { value: 1, name: '개' },
        { value: 2, name: 'L' },
        { value: 3, name: '조각' }
    ];

    let isFormVisible = false;

    function toggleFormVisibility() {
        isFormVisible = !isFormVisible;
    }

    function addItem(event) {
        event.preventDefault();
        const selectedCategory = categories.find(cat => cat.value == cat_selected)?.name || '';
        const selectedUnit = units.find(unit => unit.value == unit_selected)?.name || '';

        lists.push({
            foodname,
            volume,
            unit: selectedUnit,
            category: selectedCategory,
            purchaseDate,
            expirationDate
        });

        foodname = '';
        volume = '';
        unit_selected = '';
        cat_selected = '';
        purchaseDate = '';
        expirationDate = '';
    }
</script>

<style>
    .modal {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        visibility: hidden;
        opacity: 0;
        transition: visibility 0s, opacity 0.5s linear;
    }
    .modal.active {
        visibility: visible;
        opacity: 1;
    }
    .modal-content {
        background: white;
        padding: 20px;
        border-radius: 8px;
        width: 80%;
        max-width: 500px;
    }
</style>

<b>{data}</b>
<a href="#" on:click|preventDefault={toggleFormVisibility} class="font-serif text-lime-950 text-sm font-medium text-primary-600"> + </a>
<div class="modal {isFormVisible ? 'active' : ''}">
    <div class="modal-content">
        <form on:submit|preventDefault={addItem}>
            <div class='flex flex-wrap -mx-2 p-2'>
                <Label for="Category" class="mb-2 text-xs">Category</Label>
                <Select id="select-category" bind:value={cat_selected} style='font-size:x-small' size="sm" items={categories} placeholder="Category"/>
            </div>
            <div class="flex flex-wrap -mx-2">
                <div class='flex flex-col w-1/3 p-2'>
                    <Label for="Foodname" class="mb-2 text-xs">Foodname</Label>
                    <Input type="text" bind:value={foodname} class='border rounded border-gray-300' id="foodname" style='font-size:x-small' placeholder="Foodname" required/>
                </div>
                <div class='flex flex-col w-1/3 p-2'>
                    <Label for="Volume" class="mb-2 text-xs">Volume</Label>
                    <Input type="number" bind:value={volume} class='rounded' id="volume" style='font-size:x-small' placeholder="Volume" required />
                </div>
                <div class='flex flex-col w-1/3 p-2'>
                    <Label for="Unit" class="mb-2 text-xs">Unit</Label>
                    <Select id="select-unit" bind:value={unit_selected} class='' size="md" style='font-size:x-small' items={units} placeholder="Unit"/>
                </div>
            </div>
            <div class="flex flex-wrap -mx-2">
                <div class='flex flex-col w-1/2 p-2'>
                    <Label for="purchaseDate" class="mb-2 text-xs">Purchase Date</Label>
                    <Input type="date" bind:value={purchaseDate} class='' style='font-size:x-small' id="purchaseDate" required />
                </div>
                <div class='flex flex-col w-1/2 p-2'>
                    <Label for="expirationDate" class="mb-2 text-xs">Expiration date</Label>
                    <Input type="date" bind:value={expirationDate} class='' id="expirationDate" style='font-size:x-small' required />
                </div>
            </div>
            <div class= 'flex justify-between'>
                <Button type="button" on:click={toggleFormVisibility} class="flex text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>BACK</Button>
                <Button type="submit" class="flex text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size = 'xs'>ADD</Button>
            </div>
        </form>
    </div>
</div>
