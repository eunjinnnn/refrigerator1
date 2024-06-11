<script>
    import { onMount } from 'svelte';
    import { fetchData } from "$lib/fetchData.js";

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
</script>


{#if isLoading}
    <b>Loading...</b>
{:else if error}
    <b>Error: {error.message}</b>
{:else}
<div class='bg-zinc-50/70 flex flex-col mb-5 overflow-hidden border rounded-xl shadow-md'>
    <div class="flex justify-between items-center mb-2">
        <h2 class="text-lg font-grandstander ml-1"><strong>Your Category</strong></h2>
    </div>
</div>

{#each categories as category}
    <div class='bg-zinc-50/70 flex flex-col mb-5 overflow-hidden border rounded-xl shadow-md'>
        <div class="flex justify-center items-center px-4 py-4">
            <div class='flex items-center'>
                <p>{category.isactive}</p>
                <img src={category.img_url} class="h-6 sm:h-5" alt="ICON" />
                <p class="font-grandstander text-xl md:text-lg sm: text-md font-bold text-amber-950 ml-2 mt-2"> {category.name}</p>
            </div>
        </div>
        <div class="mx-4 border-b border-lime-950 border-opacity-30"></div>
    </div>
{/each}
{/if}