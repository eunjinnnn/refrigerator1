<script>
    import { Button, Select, Input } from 'flowbite-svelte';
    import { onMount } from 'svelte';
    import { fetchData } from "$lib/fetchData.js";
    import LoadingPage from '../loading.svelte';

    // let item_list = [
    //     { category: 1, foodname: '양파', volume: '5', unit: '개', expiration_date: '2024-05-24', purchase_date: '2024-05-20' },
    //     { category: 1, foodname: '대파', volume: '5', unit: '개', expiration_date: '2024-05-23',  purchase_date: '2024-05-20' },
    //     { category: 1, foodname: '당근', volume: '5', unit: '개', expiration_date: '2024-05-05', purchase_date: '2024-05-20' },
    //     { category: 1, foodname: '양배추', volume: '5', unit: '개', expiration_date: '2024-05-07', purchase_date: '2024-05-20' },
    //     { category: 2, foodname: '사이다', volume: '2', unit: 'L', expiration_date: '2024-05-28', purchase_date: '2024-05-20' },
    //     { category: 2, foodname: '콜라', volume: '2', unit: 'L', expiration_date: '2024-05-06', purchase_date: '2024-05-20' },
    //     { category: 3, foodname: '만두', volume: '2', unit: '개', expiration_date: '2024-05-06', purchase_date: '2024-05-20' },
    //     { category: 4, foodname: '다진마늘', volume: '10', unit: '조각', expiration_date: '2025-05-06', purchase_date: '2024-05-20' },
    // ];

    // let categories = [
    //     { value: 1, name: 'VEGETABLES' },
    //     { value: 2, name: 'DRINKS' },
    //     { value: 3, name: 'FROZEN FOOD' },
    //     { value: 4, name: 'ETC' }
    // ];

    let categories = [];
    let activeCategories = [];
    let foodItems = [];
    let units = [];
    let isLoading = true;
    let error = null;

    onMount(async () => {
        try {
            // Fetch categories
            const categoriesResponse = await fetchData('foods/categories', 'GET');
            categories = categoriesResponse;
            activeCategories = categories.filter(category => category.isactive);

            // Fetch food items
            const foodItemsResponse = await fetchData('foods/fooditems', 'GET');
            console.log('Fetched food items:', foodItemsResponse); 
            foodItems = foodItemsResponse;

            // Fetch units
            const unitsResponse = await fetchData('foods/foodunits', 'GET');
            units = unitsResponse;

            isLoading = false;
        } catch (err) {
            error = err;
            isLoading = false;
        }
    });

    let forms = [{ category: '', foodname: '', volume: '' }];

    function addForm() {
        forms = [...forms, { category: '', foodname: '', volume: '' }];
    }

    function updateForm(index, field, value) {
        forms[index][field] = value;
    }

    function filteredFoods(category) {
        return foodItems.filter(item => item.category === category);
    }
</script>

<div class='bg-zinc-50/70 flex flex-col mb-5 overflow-hidden border rounded-xl shadow-md'>
    <div class="flex justify-center items-center px-4 py-4">
        <div class='flex items-center'>
            <p class="font-grandstander text-xl md:text-lg sm: text-md font-bold text-amber-950 ml-2 mt-2"> TODAY'S COOKING</p>
        </div>
    </div>
    <div class="mx-4 border-b border-zinc-950 border-opacity-30"></div>
    <div class="container mx-auto p-4">
        {#each forms as form, index}
            <div class="flex space-x-2 mb-4">
                <Select bind:value={form.category} placeholder="Select Category">
                    {#each activeCategories as category}
                        <option value={category.value}>{category.name}</option>
                    {/each}
                </Select>
                <Select bind:value={form.foodname} placeholder="Select Food">
                    {#each filteredFoods(parseInt(form.category)) as food}
                        <option value={food.foodname}>{food.foodname}</option>
                    {/each}
                </Select>
                <Input type="number" bind:value={form.volume} placeholder="Volume" min="1" max={foodItems.find(item => item.foodname === form.foodname)?.volume || 0} />
            </div>
        {/each}
        <button on:click={addForm} class="w-full bg-zinc-200/70 text-black text-xl rounded-lg ">+</button>
    </div>
    <div class = 'flex p-4'>
        <div class = 'flex w-1/2 w-full'>
            <Button on:click={addForm} class="flex w-full border-[1px] border-zinc-500 text-xxs font-semibold font-PoetsenOne  bg-[#E8C9D5]/50 text-zinc-950 hover:bg-[#E8C9D5]">ADD FOOD DIARY</Button>
            <Button on:click={addForm} class="flex w-full border-[1px] border-zinc-500 text-xxs font-semibold font-PoetsenOne  bg-[#E8C9D5]/50 text-zinc-950 hover:bg-[#E8C9D5]">DELETE</Button>
        </div>
        
    </div> 

</div>




  