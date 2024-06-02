<script>
    import { Button, Select, Input } from 'flowbite-svelte';

    let item_list = [
        { category: 1, foodname: '양파', volume: '5', unit: '개', expiration_date: '2024-05-24', purchase_date: '2024-05-20' },
        { category: 1, foodname: '대파', volume: '5', unit: '개', expiration_date: '2024-05-23',  purchase_date: '2024-05-20' },
        { category: 1, foodname: '당근', volume: '5', unit: '개', expiration_date: '2024-05-05', purchase_date: '2024-05-20' },
        { category: 1, foodname: '양배추', volume: '5', unit: '개', expiration_date: '2024-05-07', purchase_date: '2024-05-20' },
        { category: 2, foodname: '사이다', volume: '2', unit: 'L', expiration_date: '2024-05-28', purchase_date: '2024-05-20' },
        { category: 2, foodname: '콜라', volume: '2', unit: 'L', expiration_date: '2024-05-06', purchase_date: '2024-05-20' },
        { category: 3, foodname: '만두', volume: '2', unit: '개', expiration_date: '2024-05-06', purchase_date: '2024-05-20' },
        { category: 4, foodname: '다진마늘', volume: '10', unit: '조각', expiration_date: '2025-05-06', purchase_date: '2024-05-20' },
    ];

    let categories = [
        { value: 1, name: 'VEGETABLES' },
        { value: 2, name: 'DRINKS' },
        { value: 3, name: 'FROZEN FOOD' },
        { value: 4, name: 'ETC' }
    ];

    let forms = [{ category: '', foodname: '', volume: '' }];

    function addForm() {
        forms = [...forms, { category: '', foodname: '', volume: '' }];
    }

    function updateForm(index, field, value) {
        forms[index][field] = value;
    }

    function filteredFoods(category) {
        return item_list.filter(item => item.category === category);
    }
</script>

<div class="flex justify-between items-center px-4 py-2">
    <p class="font-PoetsenOne text-sm font-semibold text-lime-950 truncate dark:text-white"># TODAY'S COOKING</p>
    <div>
        <a href="#" on:click|preventDefault={toggleFormVisibility} class="font-serif text-lime-950 text-sm font-medium text-primary-600"> + </a>
    </div>
</div>
<div class="border-b border-lime-950 border-opacity-30"></div>

<div class="container mx-auto">
    {#each forms as form, index}
        <div class="flex space-x-2 mb-4">
            <Select bind:value={form.category} placeholder="Select Category">
                {#each categories as category}
                    <option value={category.value}>{category.name}</option>
                {/each}
            </Select>
            <Select bind:value={form.foodname} placeholder="Select Food">
                {#each filteredFoods(parseInt(form.category)) as food}
                    <option value={food.foodname}>{food.foodname}</option>
                {/each}
            </Select>
            <Input type="number" bind:value={form.volume} placeholder="Volume" min="1" max={item_list.find(item => item.foodname === form.foodname)?.volume || 0} />
        </div>
    {/each}
    <Button on:click={addForm} class="bg-lime-950 text-white">+</Button>
</div>
<div class = 'flex'>
    <Button on:click={addForm} class="bg-lime-950 text-white mt-2 mr-2">ADD FOOD DIARY</Button>
    <Button on:click={addForm} class="bg-lime-950 text-white mt-2">OK</Button>
</div>



  