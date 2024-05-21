<script>
    import { Input, Label, Button, Select, Card, Alert } from 'flowbite-svelte';

    let add_lists = [];
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

    function addItem() {
        const selectedCategory = categories.find(cat => cat.value == cat_selected)?.name || '';
        const selectedUnit = units.find(unit => unit.value == unit_selected)?.name || '';
        
        lists = [
        ...lists, 
        {
            foodname: foodname,
            volume: volume,
            unit: selectedUnit,
            category: selectedCategory,
            purchaseDate: purchaseDate,
            expirationDate: expirationDate
        }
        ];
        
        foodname = '';
        volume = '';
        unit_selected = '';
        cat_selected = '';
        purchaseDate = '';
        expirationDate = '';
    }
</script>
  
<form class='container mx-auto' on:submit|preventDefault={addItem}>
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
    <div class="flex justify-end">
        <Button type="submit" color='green' class="text-xs" style="font-size: x-small;">ADD</Button>
    </div>
</form>
  
<div class="container mx-auto">
    <div class="flex flex-wrap -mx-2">
        {#each add_lists as l}
            <div class="w-1/3 p-2">
                <Card class="w-full relative">
                    <div class="flex-wrap text-center">
                        <div class="text-xs font-bold">#{l.category}</div>
                        <div class="text-xs">{l.foodname} {l.volume}{l.unit}</div>
                        <div class="text-xxs">{l.purchaseDate}</div>
                        <div class="text-xs">{l.expirationDate}</div>
                    </div>
                    <Button type='button' class='absolute top-2 right-2 p-1 text-xxs border-none rounded-full' color = 'alternative'>X</Button>
                </Card>
            </div>
        {/each}
    </div>

    {#if add_lists.length == 0}
        <!-- <Alert color="green" class='mt-2 text-center'>
            <span class="font-medium">No items!</span>
            Please add items using above form.
        </Alert> -->
        <div></div>
    {:else}
        <div class="flex justify-end">
            <Button type="submit" color='green' class="text-xs" style="font-size: x-small;">OK</Button>
        </div>
    {/if}


</div>