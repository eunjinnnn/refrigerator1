<script>
    import { onMount } from 'svelte';
    import { fetchData } from "$lib/fetchData.js";
    import { Toggle } from 'flowbite-svelte';
    import LoadingPage from '../loading.svelte';

    let categories = [];
    let isLoading = true;
    let error = null;

    onMount(async () => {
        try {
            // Fetch categories
            const categoriesResponse = await fetchData('foods/categories', 'GET');
            categories = categoriesResponse;
            isLoading = false;
        } catch (err) {
            error = err;
            isLoading = false;
        }
    });

    async function updateCategoryStatus(category, isActive) {
        try {
            const updatedCategory = { ...categoryr, isactive: isActive };
            console.log(updatedCategory)
            const response = await fetchData(`foods/categories/${category.id}`, 'PUT', updatedCategory);
            category.isactive = response.isactive;
        } catch (err) {
            console.error('Error updating category status:', err);
        }
    }
</script>

{#if isLoading}
    <LoadingPage/>
{:else if error}
    <b>Error: {error.message}</b>
{:else}
<div class='bg-zinc-50/70 flex flex-col mb-5 overflow-hidden border rounded-xl shadow-md'>
    <div class="flex justify-center items-center mb-2">
        <div class='flex items-center'>
            <h2 class="mt-2 text-lg font-grandstander text-center"><strong>Your Category</strong></h2>
        </div>
    </div>
    <div class="mx-4 border-b border-zinc-950 border-opacity-30"></div>
    {#each categories as category}
        <div class='flex items-center my-2'>
            <Toggle 
                checked={category.isactive} 
                class='scale-75 mr-4 ml-[calc(20%)]'
                on:change={(e) => updateCategoryStatus(category, e.target.checked)}
            />
            <div class='flex items-center'>
                <img src={category.img_url} class="h-6 sm:h-5" alt="ICON" />
                <p class="font-grandstander text-md md:text-lg sm:text-md {category.isactive ? 'text-amber-950' : 'text-zinc-400'} ml-2 mt-2"> {category.name}</p>
            </div>
        </div>
    {/each}
</div>
{/if}
